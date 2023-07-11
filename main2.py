import streamlit as st
import time

def introducao():
    st.write("Você é uma maga poderosa em uma missão para salvar seu parceiro.")
    time.sleep(1)
    st.write("Durante a busca, você foi capturada e agora está presa em uma dungeon misteriosa.")
    time.sleep(1)
    st.write("Seu objetivo é encontrar uma saída e escapar dessa dungeon perigosa.")
    time.sleep(1)

def escolher_porta():
    st.write("\nVocê está em uma sala com quatro portas. Cada porta tem um desafio diferente.")
    time.sleep(2)
    st.write("Escolha sabiamente. Qual porta você escolhe?")
    time.sleep(1)

    escolha = st.radio("Escolha a porta", ("Porta vermelha", "Porta azul", "Porta amarela", "Porta verde"))

    if escolha == "Porta vermelha":
        st.write("\nVocê abriu a porta vermelha e entrou em uma sala cheia de monstros!")
        time.sleep(4)
        st.write("Você lutou bravamente, mas foi derrotada... Fim de jogo!")
    elif escolha == "Porta azul":
        st.write("\nVocê abriu a porta azul e encontrou um labirinto sombrio.")
        time.sleep(4)
        st.write("Você se perdeu no labirinto e não conseguiu encontrar a saída... Fim de jogo!")
    elif escolha == "Porta amarela":
        st.write("\nVocê abriu a porta amarela e se deparou com uma sala de quebra-cabeças.")
        time.sleep(2)
        st.write("Você resolveu o quebra-cabeças com habilidade e a porta se abriu!")
        time.sleep(2)
        st.write("Você avançou para a próxima fase.")
        time.sleep(2)
        caminho_extra()
    elif escolha == "Porta verde":
        st.write("\nVocê abriu a porta verde e entrou em uma sala cheia de tesouros!")
        time.sleep(4)
        st.write("Você coletou riquezas incontáveis e escapou da dungeon com sucesso!")
        time.sleep(2)
        st.write("Você alcançou um final glorioso. Parabéns, você venceu o jogo!")

def caminho_extra():
    st.write("\nVocê saiu da dungeon com seu parceiro e agora tem a liberdade para explorar diferentes caminhos.")
    time.sleep(1)
    st.write("Escolha um dos caminhos abaixo:")
    time.sleep(1)

    escolha = st.radio("Escolha o caminho", ("Floresta encantada", "Montanhas gélidas", "Cidade misteriosa"))

    if escolha == "Floresta encantada":
        st.write("\nVocê entrou na floresta encantada e se deparou com criaturas mágicas.")
        time.sleep(4)
        st.write("Você superou os desafios da floresta e encontrou um artefato poderoso!")
        time.sleep(1)
        st.write("Você continua sua jornada com mais confiança.")
        time.sleep(1)
        st.write("A aventura continua...")
        terceira_parte()
    elif escolha == "Montanhas gélidas":
        st.write("\nVocê decidiu explorar as montanhas gélidas, enfrentando condições extremas.")
        time.sleep(4)
        st.write("Com sua determinação, você superou os desafios e encontrou um conhecimento antigo!")
        time.sleep(1)
        st.write("Esse conhecimento vai ajudá-la em futuras batalhas.")
        time.sleep(1)
        st.write("A aventura continua...")
        terceira_parte()
    elif escolha == "Cidade misteriosa":
        st.write("\nVocê chegou a uma cidade misteriosa, onde segredos ocultos esperam para serem revelados.")
        time.sleep(4)
        st.write("Você desvendou os mistérios da cidade e ganhou a gratidão de seus habitantes.")
        time.sleep(1)
        st.write("Eles lhe deram um presente especial que aumentará suas habilidades mágicas!")
        time.sleep(1)
        st.write("A aventura continua...")
        terceira_parte()

def terceira_parte():
    st.write("\nVocê agora tem novas opções para prosseguir com sua jornada.")
    time.sleep(2)
    st.write("Escolha uma das opções abaixo:")
    time.sleep(1)

    escolha = st.radio("Escolha a opção", ("Explorar uma masmorra abandonada", "Investigar uma floresta amaldiçoada", "Negociar com um clã de ladrões"))

    if escolha == "Explorar uma masmorra abandonada":
        st.write("\nVocê decidiu explorar uma masmorra abandonada cheia de perigos e mistérios.")
        time.sleep(4)
        st.write("Enquanto explora, você encontra artefatos antigos e desvenda segredos ocultos.")
        time.sleep(1)
        st.write("Sua coragem é recompensada com poderes adicionais e conhecimento valioso!")
        time.sleep(1)
        st.write("A aventura continua...")
        final()
    elif escolha == "Investigar uma floresta amaldiçoada":
        st.write("\nVocê decide investigar uma floresta amaldiçoada, onde estranhas criaturas habitam.")
        time.sleep(4)
        st.write("Durante sua investigação, você desvenda os segredos da maldição e encontra uma solução.")
        time.sleep(1)
        st.write("Você é elogiada por sua bravura e sabedoria, e recebe a gratidão das criaturas da floresta!")
        time.sleep(1)
        st.write("A aventura continua...")
        final()
    elif escolha == "Negociar com um clã de ladrões":
        st.write("\nVocê opta por negociar com um clã de ladrões para obter informações valiosas.")
        time.sleep(4)
        st.write("Você usa suas habilidades diplomáticas para ganhar a confiança do clã e obter as informações necessárias.")
        time.sleep(1)
        st.write("O clã fica impressionado com suas habilidades e oferece sua ajuda em futuras missões!")
        time.sleep(1)
        st.write("A aventura continua...")
        final()

def final():
    st.write("\nVocê enfrentou muitos desafios, superou obstáculos e se tornou uma maga lendária!")
    time.sleep(2)
    st.write("Seu parceiro foi salvo, e você deixou um legado de coragem e poder.")
    time.sleep(1)
    st.write("Parabéns por completar essa incrível aventura!")
    time.sleep(2)

def jogar_jogo():
    introducao()
    escolher_porta()

st.title("Escape")
st.write("Bem-vindo! Você está prestes a embarcar em uma aventura emocionante.")

jogar_jogo()
