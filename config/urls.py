"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencia'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicoes'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('tipo_avaliacao/', TipoAvaliacaoView.as_view(), name='tipo_avaliacao'),
    path('turma/', TurmaView.as_view(), name='turmas'),
    path('turno/', TurnosView.as_view(), name='turnos'),
    path('area_saber/', AreasSaberView.as_view(), name='area_saber'),

    
    # path('disciplina-por-curso/', DisciplinaPorCursoView.as_view(), name='disciplina_por_curso'),
]
