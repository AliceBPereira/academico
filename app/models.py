from django.db import models

# RF01 - Gerenciar pessoas
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):  # RF02 - Gerenciar ocupação de pessoas
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

# RF03 - Gerenciar instituição de ensino
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    site = models.URLField(verbose_name="Site da instituição")
    telefone = models.CharField(max_length=15, verbose_name="Telefone da instituição")
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

# RF04 - Gerenciar áreas do saber
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da área")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"

# RF05 - Gerenciar cursos
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga horária total")
    duracao_meses = models.IntegerField(verbose_name="Duração em meses")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

# RF06 - Gerenciar turnos
class Turno(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

# RF07 - Gerenciar disciplinas
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

# RF08 - Gerenciar Matrículas
class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Data Prevista de Término")

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

# RF09 - Gerenciar avaliações
class TipoAvaliacao(models.Model):  # RF15 - Manter tipos de avaliação
    nome = models.CharField(max_length=100, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"


class Avaliacao(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    nota = models.FloatField(verbose_name="Nota")
    tipoavaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return f"{self.descricao} - {self.nota}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

# RF10 - Gerenciar frequência
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina} - {self.numero_faltas}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

# RF11 - Gerenciar turmas
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

# RF13 - Gerenciar ocorrências
class Ocorrencia(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")

    def __str__(self):
        return f"{self.descricao[:30]} - {self.data}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

# RF14 - Disciplinas por cursos (utilize Inline no admin)
class DisciplinaPorCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")

    def __str__(self):
        return f"{self.curso} - {self.disciplina} - {self.turno}"

    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Cursos"
