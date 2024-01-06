#todo esse jogo é apenas uma brincadeira e tem como objetivo praticar o que foi aprendido de forma humorada e divertida
import pygame, sys, random
pygame.init()
musica_de_fundo = pygame.mixer.music.load('so_love.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.09) 

print("Seja muito bem vindo ao quiz do Lilico para conquistar a Giovanna! Are You a Karma? Because Karma is a Queen")
answer_user = input("Está pronto?(responda com sim ou nao) ")
print(answer_user)

if answer_user != "sim":
    quit()

score = 0

print("Começando...")
print("Em que ano foi lançado o filme Star Wars: Uma Nova Esperança?\n(a)1987 \n(b)1976 \n(c)1977 \n(d)1974")
resposta1 = input("Resposta: ")

if resposta1 == "c":
    print("Acertou!")
    score = score +1
else:
    print("Errou!")

print("Batman teve vários robins ao longo da história.Qual o nome do primeiro robin? \n(a)Marc Grayson \n(b)Jason Toddy \n(C)Damian Wayne \n(d)Dick Grayson")
resposta2 = input("Resposta: ")

if resposta2 == "d":
    print("Acertou!")
    score = score +1
else:
    print("Errou!")

print("Pq taylor criou o taylor’s version? \n(a)Pq a Taylor achou que deveria ter seu nome nas músicas pois as músicas eram dela e como ela que cantava as músicas ela botou o taylor’s version para mostrar que era a versão dela \n(b)Pq taylor tinha uma gravadora até que ela quis sair só que a gravadora não queria devolver as músicas para a taylor ent taylor começou a refazer as músicas para que as músicas se tornassem dela dnv \n(c)Pq foi ela quem escreveu as letras \n(d)Pq ela achou bonito")
resposta3 = input("Resposta: ")

if resposta3 == "b":
    print("Acertou!")
    score = score +1
else:
    print("Errou!")

print("Qual a menor nota que se pode tirar em Hogwarts? \n(a)T de Trasgo \n(b)P de Péssimo \n(c)D de Deplorável \n(d)T de Trouxa")
resposta4 = input("Resposta: ")

if resposta4 == "a":
    print("Acertou!")
    score = score +1
else:
    print("Errou!")

print("Qual é o maior goleador da história do Internacional? E quantos gols foram feitos por esse ex-jogador? \n(a)D'Alessandro. 79 Gols \n(b)Fernandão, 293 Gols \n(c)Falcão, 342 Gols \n(d)Carlitos, 325 Gols")
resposta5 = input("Resposta: ")

if resposta5 == "d":
    print("Acertou!")
    score = score +1
else:
    print("Errou!")

print("Quando a gente se atrasou pro filme da taylor, pra qual filme a gente resgatou ingresso pra poder entrar na sala? \n(a)FNAF \n(b)Não Abra \n(C)Trolls 3 \n(d)Assassinos da Lua das Flores")
resposta6 = input("Resposta: ")

if resposta6 == "b":
    print("Acertou!")
    score = score +1
else:
    print("Errou!")

if score >3:
    print(f"Quiz Finalizado! Sua pontuação foi {score}/6, e você está preparado para conquistar a Giovanna <3")
else:
    print(f"Quiz Finalizado! Sua pontuação foi {score}/6, infelizmente precisa se esforçar mais pra conquistar a Giovanna :(")