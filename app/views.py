from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *

# Página inicial
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# Gerenciar cidades
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        uf = request.POST.get('uf')
        Cidade.objects.create(nome=nome, uf=uf)
        messages.success(request, "Cidade adicionada com sucesso!")
        return redirect('cidades')

# Gerenciar ocupações
class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacoes.html', {'ocupacoes': ocupacoes})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        Ocupacao.objects.create(nome=nome)
        messages.success(request, "Ocupação adicionada com sucesso!")
        return redirect('ocupacoes')

# Gerenciar pessoas
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.select_related('cidade', 'ocupacao').all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        cidade_id = request.POST.get('cidade')
        ocupacao_id = request.POST.get('ocupacao')
        cidade = get_object_or_404(Cidade, id=cidade_id)
        ocupacao = get_object_or_404(Ocupacao, id=ocupacao_id)
        Pessoa.objects.create(nome=nome, cpf=cpf, email=email, cidade=cidade, ocupacao=ocupacao)
        messages.success(request, "Pessoa adicionada com sucesso!")
        return redirect('pessoas')

# Gerenciar instituição de ensino
class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.select_related('cidade').all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        site = request.POST.get('site')
        telefone = request.POST.get('telefone')
        cidade_id = request.POST.get('cidade')
        cidade = get_object_or_404(Cidade, id=cidade_id)
        InstituicaoEnsino.objects.create(nome=nome, site=site, telefone=telefone, cidade=cidade)
        messages.success(request, "Instituição adicionada com sucesso!")
        return redirect('instituicoes')

# Gerenciar áreas do saber
class AreasSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'area_saber.html', {'areas': areas})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        AreaSaber.objects.create(nome=nome)
        messages.success(request, "Área do saber adicionada com sucesso!")
        return redirect('areas_saber')

# Gerenciar cursos
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.select_related('area_saber', 'instituicao').all()
        return render(request, 'cursos.html', {'cursos': cursos})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        carga_horaria_total = request.POST.get('carga_horaria_total')
        duracao_meses = request.POST.get('duracao_meses')
        area_id = request.POST.get('area_saber')
        instituicao_id = request.POST.get('instituicao')
        area = get_object_or_404(AreaSaber, id=area_id)
        instituicao = get_object_or_404(InstituicaoEnsino, id=instituicao_id)
        Curso.objects.create(
            nome=nome,
            carga_horaria_total=carga_horaria_total,
            duracao_meses=duracao_meses,
            area_saber=area,
            instituicao=instituicao
        )
        messages.success(request, "Curso adicionado com sucesso!")
        return redirect('cursos')

# Gerenciar turnos
class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        Turno.objects.create(nome=nome)
        messages.success(request, "Turno adicionado com sucesso!")
        return redirect('turnos')

# # Gerenciar disciplinas
class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.select_related('area_saber').all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        area_id = request.POST.get('area_saber')
        area = get_object_or_404(AreaSaber, id=area_id)
        Disciplina.objects.create(nome=nome, area_saber=area)
        messages.success(request, "Disciplina adicionada com sucesso!")
        return redirect('disciplinas')

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.select_related('instituicao', 'curso', 'pessoa').all()
        instituicoes = InstituicaoEnsino.objects.all()
        cursos = Curso.objects.all()
        pessoas = Pessoa.objects.all()
        return render(request, 'matriculas.html', {
            'matriculas': matriculas,
            'instituicoes': instituicoes,
            'cursos': cursos,
            'pessoas': pessoas
        })

    def post(self, request, *args, **kwargs):
        instituicao_id = request.POST.get('instituicao')
        curso_id = request.POST.get('curso')
        pessoa_id = request.POST.get('pessoa')
        data_inicio = request.POST.get('data_inicio')
        data_previsao_termino = request.POST.get('data_previsao_termino')

        instituicao = get_object_or_404(InstituicaoEnsino, id=instituicao_id)
        curso = get_object_or_404(Curso, id=curso_id)
        pessoa = get_object_or_404(Pessoa, id=pessoa_id)

        Matricula.objects.create(
            instituicao=instituicao,
            curso=curso,
            pessoa=pessoa,
            data_inicio=data_inicio,
            data_previsao_termino=data_previsao_termino
        )

        messages.success(request, "Matrícula criada com sucesso!")
        return redirect('matriculas')
class AvaliacoesView(View):
    # Exibição das avaliações existentes
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

    # Criação de uma nova avaliação
    def post(self, request, *args, **kwargs):
        descricao = request.POST.get('descricao')
        curso_id = request.POST.get('curso')
        disciplina_id = request.POST.get('disciplina')
        nota = request.POST.get('nota')
        tipoavaliacao_id = request.POST.get('tipoavaliacao')

        # Buscar os objetos associados a partir dos IDs
        curso = Curso.objects.get(id=curso_id)
        disciplina = Disciplina.objects.get(id=disciplina_id)
        tipoavaliacao = TipoAvaliacao.objects.get(id=tipoavaliacao_id)

        # Criar a avaliação
        Avaliacao.objects.create(
            descricao=descricao,
            curso=curso,
            disciplina=disciplina,
            nota=nota,
            tipoavaliacao=tipoavaliacao
        )
        
        messages.success(request, "Avaliação criada com sucesso!")
        return redirect('avaliacoes')

# Gerenciar Cidades
class CidadesView(View):
    # Exibição das cidades existentes
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

    # Criação de uma nova cidade
    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        uf = request.POST.get('uf')

        if not nome or not uf:
            messages.error(request, "Todos os campos devem ser preenchidos.")
            return redirect('cidades')

        # Criação de uma nova cidade
        Cidade.objects.create(nome=nome, uf=uf)
        messages.success(request, "Cidade adicionada com sucesso!")
        return redirect('cidades')

    # Exclusão de uma cidade
    def delete(self, request, *args, **kwargs):
        cidade_id = kwargs.get('id')
        cidade = get_object_or_404(Cidade, id=cidade_id)
        cidade.delete()
        messages.success(request, "Cidade removida com sucesso!")
        return redirect('cidades')
    
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.select_related('curso', 'disciplina', 'pessoa').all()
        cursos = Curso.objects.all()
        disciplinas = Disciplina.objects.all()
        pessoas = Pessoa.objects.all()
        return render(request, 'frequencias.html', {
            'frequencias': frequencias,
            'cursos': cursos,
            'disciplinas': disciplinas,
            'pessoas': pessoas
        })

    def post(self, request, *args, **kwargs):
        curso_id = request.POST.get('curso')
        disciplina_id = request.POST.get('disciplina')
        pessoa_id = request.POST.get('pessoa')
        numero_faltas = request.POST.get('numero_faltas')

        curso = get_object_or_404(Curso, id=curso_id)
        disciplina = get_object_or_404(Disciplina, id=disciplina_id)
        pessoa = get_object_or_404(Pessoa, id=pessoa_id)

        Frequencia.objects.create(
            curso=curso,
            disciplina=disciplina,
            pessoa=pessoa,
            numero_faltas=numero_faltas
        )

        messages.success(request, "Frequência registrada com sucesso!")
        return redirect('frequencias')
    

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.select_related('curso', 'disciplina', 'pessoa').all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})
    
class TipoAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        # Recupera todos os tipos de avaliação
        tipos_avaliacao = TipoAvaliacao.objects.all()
        return render(request, 'tipo_avaliacao.html', {'tipos_avaliacao': tipos_avaliacao})

    def post(self, request, *args, **kwargs):
        # Cria um novo tipo de avaliação
        nome = request.POST.get('nome')
        TipoAvaliacao.objects.create(nome=nome)
        messages.success(request, "Tipo de Avaliação adicionado com sucesso!")
        return redirect('tipos_avaliacao')

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        turnos = Turno.objects.all()
        return render(request, 'turma.html', {'turmas': turmas, 'turnos': turnos})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        turno_id = request.POST.get('turno')
        turno = Turno.objects.get(id=turno_id)
        Turma.objects.create(nome=nome, turno=turno)
        messages.success(request, "Turma adicionada com sucesso!")
        return redirect('turmas')  # Redirect to the same page after creating the Turma