
como mover as faixas? calibra-se a faixa tocando as rodas com as faixas; daí assume-se a distancia do centro do veículo até as faixas, permitindo assim chegar a uma relação pixel/metro;
fixa-se esse valor referente a posição inicial das faixas, com a relação pixel/metro resolvida, soma-se a diferença da nova medição/entrada aos valores iniciais; desta forma as faixas se moverão e continuarão em angulo fixo;
ex:
rightLanePosition = [[a1, b1],
		     [a2, b2],
		     [a3, b3]]
leftLanePosition =  [[c1, d1],
		     [c2, d2],
		     [c3, d3]]

newRightValue = x
newLeftValue = y

aplicaRelacaoPixelMetro(newRightValue, newLeftValue)

rightLanePosition = [[a1+newRightValue, b1],
		     [a2+newrightValue, b2],
		     [a3+newRightValue, b3]]
leftLanePosition =  [[a1+newLeftValue, b1],
		     [a2+newLeftValue, b2],
		     [a3+newLeftValue, b3]]

canvas.coords(rightLane, rightLanePosition)
canvas.coords(leftLane, leftLanePosition)

root.update()