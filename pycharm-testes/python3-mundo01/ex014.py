larg = float(input('A largura da parede é: '))
alt = float(input('A altura da parede é: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².' .format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você vai precisar de {}l de tinta.' .format(tinta))