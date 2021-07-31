import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

varosok= {"Balmazújváros":"290", "Hajdúböszörmény":"274", "Hajdúhadház":"209", "Hajdúsámson":"200", "Hajdúszoboszló":"199", "Vámospércs":"199", "Egyek":"191",  "Derecske":"145", "Mikepércs":"119", "Hajdúdorog":"105", "Nyírábrány":"104", "Nádudvar":"89", "Hajdúnánás":"88", "Bagamér":"83", "Józsa":"81", "Tiszacsege":"77" }
label='Az esetek elkövetőinek születési hely szerinti eloszlása'
settlements = varosok.keys()
share = varosok.values()

data_per = data.groupby('type').agg(percentage =('del_tip', lambda p: p.sum() / data.sum() * 100)).round(2)

sns.set_style('whitegrid')
bar, az =  plt.subplots(figsize=(10,6))
ax =  sns.barplot(x='share', y=)