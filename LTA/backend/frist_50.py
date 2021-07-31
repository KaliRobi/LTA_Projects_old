from matplotlib import pyplot as plt
import numpy as np



varosok= {"Balmazújváros":"290", "Hajdúböszörmény":"274", "Hajdúhadház":"209", "Hajdúsámson":"200", "Hajdúszoboszló":"199", "Vámospércs":"199", "Egyek":"191",  "Derecske":"145", "Mikepércs":"119", "Hajdúdorog":"105", "Nyírábrány":"104", "Nádudvar":"89", "Hajdúnánás":"88", "Bagamér":"83", "Józsa":"81", "Tiszacsege":"77" }
label='A letratóztatottak születési hely szerinti eloszlása'
labels = varosok.keys()
sizes = varosok.values()


# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
pie, ax = plt.subplots(figsize=[10,6])
ax.axis('equal')



ax.pie(sizes, labels=labels, autopct='%1.1f%%', )
plt.title(label=label, fontsize=12, pad='5', backgroundcolor='gray' )
pie.savefig('eloszlas.png')

plt.show()
# "Budapest":"75",
# "Hajdúszovát":"70",
# "Nyírmártonfalva":"67",
# "Nagyléta":"65",
# "Nyíradony":"58",
# "Hosszúpályi":"57",
# "Nyíracsád":"56",
# "Püspökladány":"56",
# "Újfehértó":"55",
# "Nyíregyháza":"49",
# "Monostorpályi":"47"