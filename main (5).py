def linearsearchproduct(productlist , targetproduct):
    indices = []
    for index,product in enumerate(productlist):
      if product == targetproduct:
            indices.append(index)  
    return indices              
product=["shoes","boot","shoes","sandal", "shoes"]              
target="shoes"              
result= linearsearchproduct(product,target)
print(result) 