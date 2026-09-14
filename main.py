#cadastro da startup
startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}
#lista de soluçoes
solucoes_ativas = ["Firewall IA", "Scan de Vulnerablidades"]
#exibição
print("Nome da startup:", startup["nome"])
print("Segmento:", startup["segmento"])
print("Primeiro produto:", solucoes_ativas[0])

print ()
#matriz das bancadas
bancadas = [
    [1,0],
    [0,1]
]
#status bancadas
print("Bancada N1:", bancadas[0][0])
print("Bancada N2:", bancadas[0][1])
print("Bancada S1:", bancadas[1][0])
print("Bancada S2:", bancadas[1][1])

print ()
print("Legenda: 1 = Ocupado | 0 = Livre")