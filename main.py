#cadastro da startup
startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}
#lista de soluçoes
solucoes_ativas = ["Firewall IA", "Scan de Vulnerablidades"]
#exibição
print("==============================")
print("DADOS DA STARTUP")
print("==============================")
print("Nome da startup:", startup["nome"])
print("Segmento:", startup["segmento"])
print("Primeiro produto:", solucoes_ativas[0])
print("-" * 30)

#matriz das bancadas
bancadas = [
    [1,0],
    [0,1]
]
#status bancadas
print("\n==============================")
print("STATUS DAS BANCADAS")
print("==============================")
print("Bancada N1:", bancadas[0][0])
print("Bancada N2:", bancadas[0][1])
print("Bancada S1:", bancadas[1][0])
print("Bancada S2:", bancadas[1][1])
print("Legenda: 1 = Ocupado | 0 = Livre")
print("-" * 30)

arquivo = open("custos_cloud.csv", "r", encoding="utf-8")

cabecalho = arquivo.readline()
linha_1 = arquivo.readline()
linha_2 = arquivo.readline()
linha_3 = arquivo.readline()
linha_4 = arquivo.readline()

print("\n==============================")
print("CUSTOS DE INFRAESTRUTURA CLOUD")
print("==============================")
print(linha_1.strip())
print(linha_2.strip())
print(linha_3.strip())
print(linha_4.strip())
print("-" * 30)

arquivo.close()

_, custo_1_texto = linha_1.strip().split(",")
_, custo_2_texto = linha_2.strip().split(",")
_, custo_3_texto = linha_3.strip().split(",")
_, custo_4_texto = linha_4.strip().split(",")

custo_1 = float(custo_1_texto)
custo_2 = float(custo_2_texto)
custo_3 = float(custo_3_texto)
custo_4 = float(custo_4_texto)

total = custo_1 + custo_2 + custo_3 + custo_4

print("\n==============================")
print("RESUMO FINAL")
print("==============================")
print("Startup:", startup["nome"])
print("Bancada: Bancada N1")
print(f"Valor total da infraestrutura Cloud: R$ {total:.2f}")
print("-" * 30)