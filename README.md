**Dinâmica dos Fluidos: Energia Cinética, Piezométrica (Pressão) e Potencial**  

A compreensão das diferentes formas de energia em um escoamento de fluido é fundamental para o estudo da dinâmica dos fluidos. As três principais são: a energia cinética (associada à velocidade), a energia piezométrica (associada à pressão) e a energia potencial gravitacional (associada à altura). A seguir, apresentamos cada uma delas, a Equação de Bernoulli como princípio de conservação de energia, e um exemplo único e completo de aplicação.

---

## 1. Conceitos Fundamentais

### 1.1 Energia Cinética \(\left(E_{\mathrm{cin}}\right)\)

- **Definição**: É a forma de energia relacionada ao movimento do fluido.  
- **Expressão Geral**:  
  \[
    E_{\mathrm{cin}} = \frac{1}{2}\,\rho\,v^2
  \]  
  onde:  
  \(\rho\) é a densidade do fluido (em kg/m³) e \(v\) é a velocidade do escoamento (em m/s).

- **Interpretação**:  
  Se a velocidade do fluido aumenta, a energia cinética também aumenta. Em um escoamento real, a energia cinética pode se converter em outras formas de energia, como pressão ou potencial gravitacional.

---

### 1.2 Energia Piezométrica (Pressão) \(\left(E_{\mathrm{pie}}\right)\)

- **Definição**: É a energia armazenada pela ação da pressão do fluido.  
- **Expressão Geral**:  
  \[
    E_{\mathrm{pie}} = \frac{p}{\rho}
  \]  
  onde:  
  \(p\) é a pressão do fluido (em Pa) e \(\rho\) é a densidade do fluido (em kg/m³).  

  > Em muitas formulações (como na Equação de Bernoulli), essa parcela é escrita como \(\tfrac{p}{\rho\,g}\) para expressá-la em termos de altura de coluna de fluido.

- **Interpretação**:  
  Em situações de escoamento, a energia de pressão pode ser convertida em energia cinética ou potencial e vice-versa.

---

### 1.3 Energia Potencial Gravitacional \(\left(E_{\mathrm{pot}}\right)\)

- **Definição**: É a energia associada à posição do fluido em um campo gravitacional.  
- **Expressão Geral**:  
  \[
    E_{\mathrm{pot}} = g\,z
  \]  
  onde:  
  \(g\) é a aceleração da gravidade (\(\approx 9{,}81\ \mathrm{m/s^2}\)) e \(z\) é a altura em relação a um nível de referência (em m).  

- **Interpretação**:  
  Em um escoamento, se o fluido estiver em um nível mais alto, ele terá maior energia potencial que pode ser convertida em energia cinética ou de pressão.

---

## 2. Conservação de Energia: Equação de Bernoulli

Para um fluido incompressível, ideal e em escoamento permanente, a **Equação de Bernoulli** expressa a conservação das formas de energia ao longo de uma linha de corrente:

\[
  \frac{p}{\rho\,g} + \frac{v^2}{2\,g} + z = \text{constante}
\]

onde cada termo representa, respectivamente, a energia piezométrica (altura de pressão), a energia cinética (altura de velocidade) e a energia potencial gravitacional (altura de elevação) por unidade de peso do fluido.

---

## 3. Exemplo Completo: Escoamento em um Tubo com Variação de Diâmetro

**Problema Proposto**  
Considere um fluido incompressível (por exemplo, água, de densidade \(\rho\)) escoando em um **tubo horizontal** que apresenta duas seções com diâmetros diferentes. Na seção 1 (maior), o diâmetro é \(D_1\), a velocidade do fluido é \(v_1\) e a pressão é \(p_1\). Na seção 2 (menor), o diâmetro é \(D_2\). Deseja-se determinar:

1. A velocidade \(v_2\) na seção menor.  
2. A pressão \(p_2\) na seção menor.

### 3.1 Passo 1: Aplicar a Equação da Continuidade

A **Equação da Continuidade** para um fluido incompressível diz que a vazão volumétrica \(Q\) é a mesma em todas as seções do tubo:

\[
  Q = A_1 \, v_1 = A_2 \, v_2
\]

onde \(A_1\) e \(A_2\) são as áreas das seções 1 e 2, respectivamente. Como o tubo é circular:

\[
  A_1 = \frac{\pi\,D_1^2}{4} 
  \quad\quad \text{e} \quad\quad
  A_2 = \frac{\pi\,D_2^2}{4}
\]

Logo,

\[
  A_1 \, v_1 = A_2 \, v_2
  \quad \Rightarrow \quad
  \frac{\pi\,D_1^2}{4}\,v_1 = \frac{\pi\,D_2^2}{4}\,v_2
  \quad \Rightarrow \quad
  v_2 = v_1 \,\frac{D_1^2}{D_2^2}.
\]

### 3.2 Passo 2: Aplicar a Equação de Bernoulli

Para um **tubo horizontal**, podemos considerar \(z_1 = z_2\), de modo que a diferença na energia potencial gravitacional seja nula. Então, a Equação de Bernoulli entre as seções 1 e 2 fica:

\[
  \frac{p_1}{\rho\,g} + \frac{v_1^2}{2\,g} = \frac{p_2}{\rho\,g} + \frac{v_2^2}{2\,g}.
\]

Rearranjando para \(p_2\), temos:

\[
  \frac{p_2}{\rho\,g} = \frac{p_1}{\rho\,g} + \frac{v_1^2}{2\,g} - \frac{v_2^2}{2\,g}
  \quad\Rightarrow\quad
  p_2 = p_1 + \frac{1}{2}\,\rho\,(v_1^2 - v_2^2).
\]

Contudo, já sabemos \(v_2\) do passo anterior (\(v_2 = v_1 \,\tfrac{D_1^2}{D_2^2}\)). Portanto, basta substituir o valor de \(v_2\) na expressão acima.

---

### 3.3 Resultados

1. **Velocidade na Seção Menor**:  
   \[
     v_2 = v_1 \,\frac{D_1^2}{D_2^2}.
   \]

2. **Pressão na Seção Menor**:  
   \[
     p_2 = p_1 + \frac{1}{2}\,\rho\,\bigl[v_1^2 - \bigl(v_1 \tfrac{D_1^2}{D_2^2}\bigr)^2\bigr]
     \;=\;
     p_1 + \frac{1}{2}\,\rho\,\Bigl[v_1^2 - v_1^2 \Bigl(\tfrac{D_1^2}{D_2^2}\Bigr)^2\Bigr].
   \]

---

## 4. Interpretação dos Resultados

1. **Energia Cinética**:  
   Como \(v_2 > v_1\) (assumindo \(D_2 < D_1\)), a velocidade aumenta na seção menor. Consequentemente, a parcela de energia cinética aumenta.

2. **Energia Piezométrica (Pressão)**:  
   Se a velocidade cresce, a pressão diminui (ao comparar seção 2 com seção 1). Esse decréscimo de pressão demonstra que parte da energia de pressão foi convertida em energia cinética.

3. **Energia Potencial**:  
   Por ser um tubo horizontal (\(z_1 = z_2\)), a energia potencial gravitacional permaneceu constante ao longo do escoamento; portanto, não há variação de altura que impacte essa forma de energia.

---

## Conclusão

Este exemplo ilustra como as **equações de continuidade** e **Bernoulli** se complementam para analisar o comportamento de um fluido incompressível que escoa em um duto com variação de diâmetro. Vemos claramente como a **energia cinética**, a **energia piezométrica** (pressão) e a **energia potencial gravitacional** interagem e se convertem de uma forma para outra, mantendo a **conservação da energia** no escoamento ideal.
