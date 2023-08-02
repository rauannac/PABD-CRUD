import streamlit as st

import controller.cliente as cliente

def deletar():
    st.title('Deletar Dados')
    
    with st.form(key='delete'):
        input_id = st.number_input(label= 'Insira o Id:', format ='%d', step=1)
        
        buttom_submit = st.form_submit_button('Deletar')
        
        if buttom_submit:
            cliente.deletar(int(input_id))
            st.success('Usuário Deletado com sucesso')