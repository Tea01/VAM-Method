# Vogel Yaklaşım Yöntemi (VAM)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/faridnec/vogels-approx-method/blob/farid-main/vogels_am.ipynb)

![vogel_result](https://github.com/faridnec/vogels-approx-method/blob/main/img/output.png?raw=true)

## Genel Bakış
Yukarıdaki çıktı için örnek taşıma problemi aşağıdaki gibidir:
```markdown
                            ------------------------------------------------------------
                                    | Mağaza 1 | Mağaza 2 | Mağaza 3 | Mağaza 4 | Arz  
                            ------------------------------------------------------------
                            Fabrika 1 |   10    |   19    |   5    |   7     |   22    
                            Fabrika 2 |   13    |   2     |   7    |   8     |   25  
                            Fabrika 3 |   15    |   18    |   6    |   14    |   10  
                            ------------------------------------------------------------ 
                            Talep     |   8     |   8     |   12   |   29    |   57     
                            ------------------------------------------------------------
```
## Giriş
Vogel'in Yaklaşık Yöntemi (VAM), doğrusal programlamadaki taşıma problemlerini çözmek için kullanılan bir algoritmadır. Bir taşıma problemi, birden çok tedarikçiden birden çok tüketiciye mal taşımanın maliyetini minimize etmeyi içerir. Vogel'in yöntemi, başlangıçta uygun bir çözüm bulmak için bir iteratif yaklaşım sağlar, bu çözüm daha sonra diğer optimizasyon teknikleri kullanılarak iyileştirilebilir.

Referans:
BYJU's. (s.t.). Vogel's Approximation Method. BYJU's. https://byjus.com/maths/vogels-approximation-method/

Proje yapısı:
```plaintext
vam-method/
|-- img/
|-- modules/
|   |-- vam.py          # VAM algoritması
|   |-- utils.py        # VAM dışında yardımcı işlev & stil
|-- main_script.py      # VAM'ı çalıştırma
|-- vogels_am.ipynb     # yöntemin açıklaması
└── README.md   
```

## Kurulum
Bu proje, sisteminizde pip yüklü olduğunu varsayarak numpy ve pandas kütüphanesini yükleyiniz
```bash
# NumPy Kurulumu
pip install numpy

# Pandas Kurulumu
pip install pandas
```

## Çıktı
Algoritmanın senaryo ve stilleme kullanılarak uygulanışını `vogels_am.ipynb` [buradan](https://github.com/faridnec/vogels-approx-method/blob/main/vogels_am.ipynb) kontrol edebilirsiniz.

Jupyter notebook üzerindeki çıktı örneği:

![Pandas Çıktısı](https://github.com/faridnec/vogels-approx-method/blob/main/img/jn_output.png?raw=true)

> veya

Bu komutu kullanarak main_script.py'yi çalıştırarak:

```bash
python main_script.py
```
Önceki örneğin çıktısı:
```markdown
// Iteration and process will be shown here ...

Total Cost (Optimized): 386 units

Transportation Plan:
[[ 8  0  2 12]
 [ 0  8  0 17]
 [ 0  0 10  0]]
```