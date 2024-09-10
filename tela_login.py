#%% Bibliotecas
import streamlit as st
from sql_alchemy import ler_todos_usuarios
from time import sleep

#%% Funções
# Tela de login
def login():
    with st.container(border=True):
        st.markdown('Bem-vindo a tela de login')
        usuarios = ler_todos_usuarios()
        usuarios = {usuario.nome: usuario for usuario in usuarios}
        nome_usuario = st.selectbox('Seleciona o usuario', list(usuarios.keys()))
        senha = st.text_input('Digite sua senha', type='password')

        # Verifica o acesso do usuario
        if st.button('Logar'):
            usuario = usuarios[nome_usuario]
            if usuario.verifica_senha(senha):
                st.success('Login efetuado com sucesso!')
                st.session_state['usuario'] = usuario
                st.session_state['logado'] = True
                sleep(1)
                st.rerun()
            else:
                st.error('Senha incorreta')


def main():
    # Cria a variavel 'logado'
    if not 'logado' in st.session_state:
        st.session_state['logado'] = False

    # Se não estiver logado vai para a tela de login()
    if not st.session_state['logado']:
        login()
    # Se logar aparece a mensagem abaixo
    else:
        st.markdown('# Bem-vindo ao WebApp')

if __name__ == '__main__':
    main()



