def main(distancia):
  if distancia <= 200:
    return distancia*0.5
  elif distancia <= 400:
    return distancia*0.45
  else:
    return distancia*0.35