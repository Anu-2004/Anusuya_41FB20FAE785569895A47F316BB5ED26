def linearSearchProduct(productList, targetPoduct):
  indices = []
  for index,Product in enumerate(productList):
      if product == targetProduct:
         indices.append(index)

  return indices

#Example usage:
product = ["rose","sunflower","rose","lotus","rose"]
target = "rose"
target2 = "apple"
result = linearSearchProduct(product, target)
print(result)