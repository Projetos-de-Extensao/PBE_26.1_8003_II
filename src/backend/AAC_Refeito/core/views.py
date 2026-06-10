from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Usuario, Aluno, Coordenador, OrgAcademica, AtividadeComplementar, AtividadeInterna, TipoAtividade


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)

            if usuario.perfil == Usuario.Perfil.ALUNO:
                return redirect("dashboard_aluno")
            elif usuario.perfil == Usuario.Perfil.COORDENADOR:
                return redirect("dashboard_coordenador")
            elif usuario.perfil == Usuario.Perfil.ORG:
                return redirect("dashboard_organizacao")

        return render(request, "core/login.html", {"erro": "Usuário ou senha inválidos."})

    return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_aluno(request):
    if request.user.perfil != Usuario.Perfil.ALUNO:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")
    aluno = Aluno.objects.filter(usuario=request.user).first()

    if not aluno:
        messages.error(request, "Perfil de aluno não encontrado.")
        return redirect("login")

    total = aluno.atualizar_total_horas()
    meta = 150
    percentual = round((total / meta) * 100, 2)

    atividades_internas = AtividadeInterna.objects.all()
    atividades_externas = AtividadeComplementar.objects.filter(aluno=aluno)

    return render(request, "core/dashboard_aluno.html", {
        "aluno": aluno,
        "total": total,
        "meta": meta,
        "percentual": percentual,
        "atividades_internas": atividades_internas,
        "atividades_externas": atividades_externas,
    })


@login_required
def dashboard_coordenador(request):
    if request.user.perfil != Usuario.Perfil.COORDENADOR:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")
    atividades_pendentes = AtividadeComplementar.objects.filter(
        status=AtividadeComplementar.Status.PENDENTE
    )

    return render(request, "core/dashboard_coordenador.html", {
        "atividades_pendentes": atividades_pendentes,
    })


@login_required
def dashboard_organizacao(request):
    
    if request.user.perfil != Usuario.Perfil.ORG:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")
    organizacao = OrgAcademica.objects.filter(usuario=request.user).first()
    atividades_internas = AtividadeInterna.objects.filter(organizacao=organizacao)

    return render(request, "core/dashboard_organizacao.html", {
        "organizacao": organizacao,
        "atividades_internas": atividades_internas,
    })

@login_required
def cadastrar_atividade_interna(request):
    if request.user.perfil not in [
        Usuario.Perfil.COORDENADOR,
        Usuario.Perfil.ORG
    ]:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")

    if request.method == "POST":

        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        carga_horaria = request.POST.get("carga_horaria")
        tipo_atividade_id = request.POST.get("tipo_atividade")

        tipo_atividade = TipoAtividade.objects.get(
            id=tipo_atividade_id
        )

        atividade = AtividadeInterna(
            titulo=titulo,
            descricao=descricao,
            carga_horaria=carga_horaria,
            tipo_atividade=tipo_atividade
        )

        if request.user.perfil == Usuario.Perfil.COORDENADOR:
            atividade.coordenador = Coordenador.objects.get(
                usuario=request.user
            )

        elif request.user.perfil == Usuario.Perfil.ORG:
            atividade.organizacao = OrgAcademica.objects.get(
                usuario=request.user
            )

        atividade.save()

        messages.success(
            request,
            "Atividade interna cadastrada com sucesso!"
        )

        if request.user.perfil == Usuario.Perfil.COORDENADOR:
            return redirect("dashboard_coordenador")

        return redirect("dashboard_organizacao")

    tipos = TipoAtividade.objects.all()

    return render(
        request,
        "core/cadastrar_atividade_interna.html",
        {"tipos": tipos}
    )

@login_required
def participar_atividade_interna(request, atividade_id):
    if request.user.perfil != Usuario.Perfil.ALUNO:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")
    aluno = get_object_or_404(Aluno, usuario=request.user)
    atividade = get_object_or_404(AtividadeInterna, id=atividade_id)

    atividade.participantes.add(aluno)

    messages.success(request, "Participação registrada com sucesso!")
    return redirect("dashboard_aluno")

@login_required
def cadastrar_atividade_externa(request):
    if request.user.perfil != Usuario.Perfil.ALUNO:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")
    aluno = Aluno.objects.filter(usuario=request.user).first()

    if not aluno:
        messages.error(request, "Perfil de aluno não encontrado.")
        return redirect("login")

    if request.method == "POST":
        descricao = request.POST.get("descricao")
        carga_horaria = request.POST.get("carga_horaria")
        tipo_atividade_id = request.POST.get("tipo_atividade")

        tipo_atividade = TipoAtividade.objects.get(id=tipo_atividade_id)

        AtividadeComplementar.objects.create(
            aluno=aluno,
            descricao=descricao,
            carga_horaria_solicitada=carga_horaria,
            tipo_atividade=tipo_atividade,
            status=AtividadeComplementar.Status.PENDENTE
        )

        messages.success(request, "Atividade externa cadastrada com sucesso!")
        return redirect("dashboard_aluno")

    tipos = TipoAtividade.objects.all()

    return render(request, "core/cadastrar_atividade_externa.html", {
        "tipos": tipos
    })

@login_required
def aprovar_atividade(request, atividade_id):
    if request.user.perfil != Usuario.Perfil.COORDENADOR:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")
    coordenador = Coordenador.objects.filter(usuario=request.user).first()

    if not coordenador:
        messages.error(request, "Apenas coordenadores podem aprovar atividades.")
        return redirect("dashboard_coordenador")

    atividade = get_object_or_404(AtividadeComplementar, id=atividade_id)

    if request.method == "POST":
        carga = request.POST.get("carga_horaria_validada")
        justificativa = request.POST.get("justificativa", "")

        try:
            carga_int = int(carga) if carga else None
        except (ValueError, TypeError):
            messages.error(request, "A carga horária deve ser um número inteiro.")
            return redirect("dashboard_coordenador")

        atividade.aprovar(
            coordenador=coordenador,
            carga_horaria_validada=carga_int,
            justificativa=justificativa
        )

        messages.success(request, "Atividade aprovada com sucesso!")
        return redirect("dashboard_coordenador")

    return render(request, "core/aprovar_atividades.html", {
        "atividade": atividade
    })

@login_required
def reprovar_atividade(request, atividade_id):
    if request.user.perfil != Usuario.Perfil.COORDENADOR:
        messages.error(request, "Acesso não autorizado.")
        return redirect("login")
    coordenador = Coordenador.objects.filter(usuario=request.user).first()

    if not coordenador:
        messages.error(request, "Apenas coordenadores podem reprovar atividades.")
        return redirect("dashboard_coordenador")

    atividade = get_object_or_404(AtividadeComplementar, id=atividade_id)

    if request.method == "POST":
        justificativa = request.POST.get("justificativa")

        if not justificativa:
            messages.error(request, "Informe uma justificativa para reprovar.")
            return redirect("reprovar_atividade", atividade_id=atividade.id)

        atividade.reprovar(
            coordenador=coordenador,
            justificativa=justificativa
        )

        messages.success(request, "Atividade reprovada com sucesso!")
        return redirect("dashboard_coordenador")

    return render(request, "core/reprovar_atividade.html", {
        "atividade": atividade
    })