import matplotlib.pyplot as plt

numerador = 3
denominador = 5
vlr = 1/denominador
v = []
for i in range(0,denominador):
    v.append(vlr)

colors = []
for i in range(0,numerador):
    colors.append("#e5e619")
for i in range(0,denominador-numerador):
    colors.append("#FFFFFF")

wedge_properties = {"edgecolor":"k",'linewidth': 2}

plt.pie(v, colors=colors, startangle=30,
           counterclock=False, shadow=True, wedgeprops=wedge_properties,
           autopct="", pctdistance=0.7, frame=False)
plt.axis('off')

plt.box(False)

nome = str(numerador) + '-' + str(denominador) + '.png'
plt.savefig(nome, transparent = True, bbox_inches='tight', pad_inches=0)

plt.show()
