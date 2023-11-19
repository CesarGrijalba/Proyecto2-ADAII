% Use this editor as a MiniZinc scratch book
% Parámetros del problema
int: J = 3;  % Número de unidades térmicas
int: K = 3;  % Número de intervalos de tiempo (horizonte de planificación)
array[1..J] of int: Ej = [20,18,5];  % Costo de encender cada unidad térmica
array[1..J] of float: Aj = [0.5,0.3,1.0];  % Costo de apagar cada unidad térmica
array[1..J] of float: Gj = [0,0,0];
array[1..J] of int: Fj = [0,0,0];  % Costo fijo de cada unidad térmica
array[1..J] of float: Vj = [0.100,0.125,0.150];  % Costo variable proporcional a la potencia

array[1..J] of int: Pj = [50,80,40];   % Límite superior de generación de potencia
array[1..J] of int: Pj_ = [350,200,140];  % Límite inferior de generación de potencia
array[1..J] of int: Supj = [200,100,100];  % Límite superior de ampliación de potencia
array[1..J] of int: Infj = [300,150,100];  % Límite inferior de reducción de potencia

array[1..K] of int: Dk = [150,500,400];  % Demanda global en cada intervalo de tiempo
array[1..K] of int: Rk = [15,50,40];  % Reserva para cada intervalo de tiempo

% Variables de decisión
array[1..J, 1..K] of var 0..1: Encendido;  % 1 si la unidad térmica j está encendida en el intervalo k, 0 en caso contrario
array[1..J, 1..K] of var int: Potencia;    % Potencia generada por la unidad térmica j en el intervalo k

%Restrcciones
%Potencia mayor a cero
constraint forall(j in 1..J, k in 1..K)(Potencia[j,k] >= 0);
%Limite superior
constraint forall(j in 1..J, k in 1..K)(Potencia[j,k] <= Pj_[j]);
%Lmite de ampliacion
constraint forall(j in 1..J, k in 2..K)(Encendido[j,k] == 1 -> Potencia[j,k] <= Infj[j]);
%Limite de reduccion
constraint forall(j in 1..J, k in 2..K)(Encendido[j,k] == 1 -> Potencia[j,k] >= Supj[j]);
%Asignacion de potencia
constraint forall(k in 1..K)(sum(j in 1..J)(Potencia[j,k]*Encendido[j,k]) >= Dk[k]+Rk[k] );
%limite inferior
constraint forall(j in 1..J, k in 1..K)(Encendido[j,k] == 1 -> Potencia[j,k] >= Pj[j]);

%Funcion objetivo

var float: costoE = sum(j in 1..J,k in 1..K)(Encendido[j,k]*Ej[j]);
var float: costoA = 0;
constraint forall(j in 2..J, k in 2..K) (
  (Encendido[j-1, k] == 1 /\ Encendido[j, k] == 0) ->
    costoA = costoA + Aj[j]
);
var float: costo_total = costoE + costoA;

solve minimize costo_total;

% Output
output ["Costo =\(costo_total)\n"]++
       ["Encendido =\n"] ++
       ["[| " ++ concat([if k < K then "\(Encendido[j, k]), " else "\(Encendido[j, k]) |\n " endif | j in 1..J, k in 1..K]) ++ "];\n"] ++
       ["Potencia =\n"] ++
       ["[| " ++ concat([if k < K then "\(Potencia[j, k]), " else "\(Potencia[j, k]) |\n " endif | j in 1..J, k in 1..K]) ++ "];\n"];