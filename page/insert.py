import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados do Usuário')
    
    with st.form(key='insert'):
        input_id = st.number_input(label= 'Insira o Id:', format ='%d', step=1)
        input_name = st.text_input(label='Insira o nome:')
        input_phone = st.text_input(label='Insira o telefone:')
        input_email = st.text_input(label='Insira o email:')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_phone, input_email)
            st.success('Usuário incluido com sucesso')

            
