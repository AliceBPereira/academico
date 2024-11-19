from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *

# Página inicial
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# # Gerenciar cidades
# class CidadesView(View):
#     def get(self, request, *args, **kwargs):
#         cidades = Cidade.objects.all()
#         return render(request, 'cidade.html', {'cidades': cidades})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         uf = request.POST.get('uf')
#         Cidade.objects.create(nome=nome, uf=uf)
#         messages.success(request, "Cidade adicionada com sucesso!")
#         return redirect('cidades')

# # Gerenciar ocupações
# class OcupacoesView(View):
#     def get(self, request, *args, **kwargs):
#         ocupacoes = Ocupacao.objects.all()
#         return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         Ocupacao.objects.create(nome=nome)
#         messages.success(request, "Ocupação adicionada com sucesso!")
#         return redirect('ocupacoes')

# # Gerenciar pessoas
# class PessoasView(View):
#     def get(self, request, *args, **kwargs):
#         pessoas = Pessoa.objects.select_related('cidade', 'ocupacao').all()
#         return render(request, 'pessoa.html', {'pessoas': pessoas})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         cpf = request.POST.get('cpf')
#         email = request.POST.get('email')
#         cidade_id = request.POST.get('cidade')
#         ocupacao_id = request.POST.get('ocupacao')
#         cidade = get_object_or_404(Cidade, id=cidade_id)
#         ocupacao = get_object_or_404(Ocupacao, id=ocupacao_id)
#         Pessoa.objects.create(nome=nome, cpf=cpf, email=email, cidade=cidade, ocupacao=ocupacao)
#         messages.success(request, "Pessoa adicionada com sucesso!")
#         return redirect('pessoas')

# # Gerenciar instituição de ensino
# class InstituicoesView(View):
#     def get(self, request, *args, **kwargs):
#         instituicoes = InstituicaoEnsino.objects.select_related('cidade').all()
#         return render(request, 'instituicao.html', {'instituicoes': instituicoes})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         site = request.POST.get('site')
#         telefone = request.POST.get('telefone')
#         cidade_id = request.POST.get('cidade')
#         cidade = get_object_or_404(Cidade, id=cidade_id)
#         InstituicaoEnsino.objects.create(nome=nome, site=site, telefone=telefone, cidade=cidade)
#         messages.success(request, "Instituição adicionada com sucesso!")
#         return redirect('instituicoes')

# # Gerenciar áreas do saber
# class AreasSaberView(View):
#     def get(self, request, *args, **kwargs):
#         areas = AreaSaber.objects.all()
#         return render(request, 'area_saber.html', {'areas': areas})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         AreaSaber.objects.create(nome=nome)
#         messages.success(request, "Área do saber adicionada com sucesso!")
#         return redirect('areas_saber')

# # Gerenciar cursos
# class CursosView(View):
#     def get(self, request, *args, **kwargs):
#         cursos = Curso.objects.select_related('area_saber', 'instituicao').all()
#         return render(request, 'curso.html', {'cursos': cursos})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         carga_horaria_total = request.POST.get('carga_horaria_total')
#         duracao_meses = request.POST.get('duracao_meses')
#         area_id = request.POST.get('area_saber')
#         instituicao_id = request.POST.get('instituicao')
#         area = get_object_or_404(AreaSaber, id=area_id)
#         instituicao = get_object_or_404(InstituicaoEnsino, id=instituicao_id)
#         Curso.objects.create(
#             nome=nome,
#             carga_horaria_total=carga_horaria_total,
#             duracao_meses=duracao_meses,
#             area_saber=area,
#             instituicao=instituicao
#         )
#         messages.success(request, "Curso adicionado com sucesso!")
#         return redirect('cursos')

# # Gerenciar turnos
# class TurnosView(View):
#     def get(self, request, *args, **kwargs):
#         turnos = Turno.objects.all()
#         return render(request, 'turno.html', {'turnos': turnos})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         Turno.objects.create(nome=nome)
#         messages.success(request, "Turno adicionado com sucesso!")
#         return redirect('turnos')

# # Gerenciar disciplinas
# class DisciplinasView(View):
#     def get(self, request, *args, **kwargs):
#         disciplinas = Disciplina.objects.select_related('area_saber').all()
#         return render(request, 'disciplina.html', {'disciplinas': disciplinas})

#     def post(self, request, *args, **kwargs):
#         nome = request.POST.get('nome')
#         area_id = request.POST.get('area_saber')
#         area = get_object_or_404(AreaSaber, id=area_id)
#         Disciplina.objects.create(nome=nome, area_saber=area)
#         messages.success(request, "Disciplina adicionada com sucesso!")
#         return redirect('disciplinas')
