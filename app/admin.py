from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Pessoa, InstituicaoEnsino, AreaSaber, Curso,
    Turno, Disciplina, Matricula, TipoAvaliacao, Avaliacao,
    Frequencia, Turma, Ocorrencia, DisciplinaPorCurso
)

# Inline para disciplinas por curso
class DisciplinaPorCursoInline(admin.TabularInline):
    model = DisciplinaPorCurso
    extra = 1
    fields = ('curso', 'disciplina', 'turno', 'carga_horaria')

# Inline para matrícula
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1
    fields = ('instituicao', 'curso', 'data_inicio', 'data_previsao_termino')

# Inline para frequência
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1
    fields = ('curso', 'disciplina', 'pessoa', 'numero_faltas')

# Inline para avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1
    fields = ('descricao', 'curso', 'disciplina', 'nota', 'tipoavaliacao')

# Inline para ocorrências
class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1
    fields = ('descricao', 'data', 'curso', 'disciplina', 'pessoa')

# Registro com Inline para Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria_total', 'duracao_meses', 'area_saber', 'instituicao')
    inlines = [DisciplinaPorCursoInline]

# Registro com Inline para Pessoa
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'cidade', 'ocupacao')
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]

# Registro com Inline para Disciplina
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber')
    inlines = [AvaliacaoInline, FrequenciaInline, OcorrenciaInline]

# Registro para outras models sem Inlines
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'telefone', 'cidade')

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('instituicao', 'curso', 'pessoa', 'data_inicio', 'data_previsao_termino')

@admin.register(TipoAvaliacao)
class TipoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'curso', 'disciplina', 'nota', 'tipoavaliacao')

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('curso', 'disciplina', 'pessoa', 'numero_faltas')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno')

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'curso', 'disciplina', 'pessoa')

@admin.register(DisciplinaPorCurso)
class DisciplinaPorCursoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'disciplina', 'turno', 'carga_horaria')
