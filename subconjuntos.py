def gerar_subconjuntos(conjunto):
    subconjuntos = [[]]

    for i in range(0,len(conjunto)):
        for j in range(0,len(subconjuntos)):
            # Para cada item do conjunto
                # Para cada item ja existente no array sendo gerado
                    # Se adiciona novos itens
                        # E cada novo item é a interação atual do array de arrays + a interação atual do conjunto
            subconjunto = subconjuntos[j].copy()
            subconjunto = subconjunto + [conjunto[i]]
            subconjuntos = subconjuntos + [subconjunto]

    return subconjuntos

if __name__ == '__main__':
    print(gerar_subconjuntos([1,2,4]))