"""
Cada aluno pode se inscrever em um curso, mas antes a plataforma precisa verificar se há vagas disponíveis;
Se houver vagas, o aluno deve ser confirmado na turma e a vaga deve ser reduzida;
Se não houver vagas, o aluno deve ser notificado de que a turma está lotada;
Se um aluno já estiver inscrito, ele não pode se inscrever novamente no mesmo curso

"""

import asyncio

class Enroll:
    def __init__(self):
        self.cursos = {
            "Python Avançado": {"vagas": 3, "inscritos": []},
            "Java para Iniciantes": {"vagas": 1, "inscritos": []},
            "Machine Learning": {"vagas": 0, "inscritos": []},
        }

    async def inscreverAluno(self, nome, curso):
        if self.cursos[curso]['vagas'] > 0:
            if nome not in self.cursos[curso]['inscritos']:
                self.cursos[curso]['inscritos'].append(nome)
                self.cursos[curso]['vagas'] -= 1
                print(f"Inscrição confirmada de {nome} no curso {curso}")
            else:
                print(f"{nome} já se inscreveu no curso {curso}")
        else:
            print(f"Vagas esgotadas para o curso {curso}")

async def main():
    enroll = Enroll()
    alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
    ]

    tarefas = [
        enroll.inscreverAluno(aluno['nome'], aluno['curso'])
        for aluno in alunos
    ]
    await asyncio.gather(*tarefas)
    print("Todas as inscrições foram processadas!")

asyncio.run(main())