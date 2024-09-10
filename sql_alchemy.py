# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:09:54 2024

@author: leoja
"""

#%% Bibliotecas
from pathlib import Path
from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import os
import sys
from werkzeug.security import generate_password_hash, check_password_hash


#%% Diretorio
pasta_atual = Path('__file__').parent
PATH_TO_BD = pasta_atual / 'bd_usuarios.sqlite'


#%% Classe
class Base(DeclarativeBase):
    pass

class Usuario(Base):
    # Nome da tabela
    __tablename__ = 'usuarios'
    
    # Colunas
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)
    
    def __repr__(self):
        return f'Usuario {self.id=}, {self.nome=}'
    
    def define_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def verifica_senha(self, senha):
        return check_password_hash(self.senha, senha)

# Cria a base de dados
engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine)



#%% CRUD
# Função para inserir dados na tabela
def cria_usuarios(
        nome,
        senha,
        email,
        **kwargs
):
    with Session(bind=engine) as session:
        usuario = Usuario(
            nome=nome,
            email=email,
            **kwargs
        )
        usuario.define_senha(senha)
        session.add(usuario)
        session.commit()

# Função para ler todos os dados
def ler_todos_usuarios():
    with Session(bind=engine) as session:
        comando_sql = select(Usuario)
        usuarios = session.execute(comando_sql).fetchall()
        usuarios = [user[0] for user in usuarios]
        return usuarios

# Função para selecionar um dado específico  
def ler_usario_id(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        return usuarios[0][0]
    

    
# Update na tabela
def modifica_usuario_old(
        id, 
        nome=None,
        senha=None,
        email=None,
        acesso_gestor=None
        ):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            if nome:
                usuario[0].nome = nome
            if senha:
                usuario[0].senha = senha
            if email:
                usuario[0].email = email
            if not acesso_gestor is None:
                usuario[0].acesso_gestor = acesso_gestor
        session.commit()

def modifica_usuario(id, **kwargs):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            for key,value in kwargs.items():
                if key == 'senha':
                    usuario[0].define_senha(value)
                else:
                    setattr(usuario[0], key, value)
                setattr(usuario[0], key, value)
        session.commit()

# Delete na base de dados
def deleta_usuario(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            session.delete(usuario[0])
        session.commit()

if __name__ == '__main__':
    # cria_usuarios(
    #     nome='Victor Syma',
    #     senha='senha',
    #     email='email.com',
    # )

    # usuarios = ler_todos_usuarios()
    # usuario_0 = usuarios[0]
    # print(usuario_0)
    # print(usuario_0.nome,usuario_0.senha,usuario_0.email)

    # usuario_leo = ler_usario_id(id=1)
    # print(usuario_leo)
    # print(usuario_leo.nome,usuario_leo.senha,usuario_leo.email)

    # modifica_usuario(id=1, nome='Teste', senha='TESTE')

    # deleta_usuario(id=2)

    # cria_usuarios(
    #     nome='Leonardo Syma',
    #     senha='senha',
    #     email='email.com',
    # )

    usuario_leo = ler_usario_id(id=1)
    print(usuario_leo.verifica_senha('senha'))


