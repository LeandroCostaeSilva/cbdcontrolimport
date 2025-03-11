import streamlit as st
st.set_page_config(page_title="CBD PRICE IMPORT CONTROL", page_icon=":loudspeaker:")
st.title("APP CBD PRICE IMPORT CONTROL")                
st.write("INFORME APENAS OS VALORES NUMÉRICOS SOLICITADOS E CLIQUE NO BOTÃO CALCULAR!")
st.write("Esse comparativo não se aplica a produtos de Cannabis que tenham THC combinado ou tenham perfil full espectrum!")
col1, col2 = st.columns(2)
with col1:
    st.header("Parâmetros de Entrada")

#dados principais
preco_internacional = st.number_input("Preço internacional do produto de cannabis (US$)", min_value=10.0, step=1.0)
concentracao_cbd = st.number_input("Informe a concentração do CBD no produto em miligrama por mililitro", min_value=5.0, step=1.0)
vol = st.number_input("Informe o volume do frasco do produto em mililitro", min_value=5.0, step=5.0 )
usd = st.number_input("Informe a cotação do dólar na data da importação", min_value=5.0, step=0.1)
frete = st.number_input("Informe o valor do frete internacional em dólar", min_value=0.0, step=10.0)
armazenagem = st.number_input("Informe o número de dias estimado de armazenagem da carga importada no recinto", min_value=0.0, step=1.0)
number_frascos = st.number_input("Informe o número de frascos do produto importado", min_value=1.0, step=1.0)
outras_siscomex = st.number_input("Informe o custo em moeda nacional do serviço de despachante e de taxas siscomex dessa importação", min_value=0.0, step=50.0)

with col2:
    st.header("Análise comparativa de custo da importação de CBD")
    if st.button("Calcular"):
        try:
            teorcbd = concentracao_cbd * vol
            preco_brl = preco_internacional * usd
            preco_brl_tributado = preco_brl * 1.6
            frete_brl = frete * usd
            preco_final = preco_brl_tributado + (frete_brl / number_frascos + armazenagem * 100 / number_frascos + outras_siscomex / number_frascos)
            valor_cbd = preco_final / teorcbd

            if valor_cbd >= 0.48:
                retorno_condicional = preco_final / teorcbd
                st.write (
                    "<p style='color: #FF4444; background-color: #4D0000; padding: 10px;'>"
                    "ATENÇÃO: importação não vantajosa, já que existe CBD no mercado nacional com melhor preço!</p>",
                    unsafe_allow_html=True
                )
            elif valor_cbd < 0.48:
                retorno_condicional = preco_final / teorcbd
                st.write(
                    "<p style='color: #90EE90; background-color: #002200; padding: 8px; border-radius: 5px;'>"
                    "Importação vantajosa considerando os custos do produto e da importação!</p>",
                    unsafe_allow_html=True
                )
            else:
                st.write("repita a operação e revise os dados")

        except Exception as e:
            st.error(f"Erro nos cálculos: {str(e)}")
    else:
        st.warning("Preencha os dados e clique em calcular")

