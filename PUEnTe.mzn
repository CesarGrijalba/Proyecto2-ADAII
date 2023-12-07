% Use this editor as a MiniZinc scratch book

% PARAMETROS

int: J; % Número de UTPEEs
int: K; % Intervalos de planificacion
array[1..J] of int: E; % Costo de encender la UTPEE j
array[1..J] of float: A; % Costo de apagar la UTPEE j
array[1..J] of 0..1: G; % Indicador de si la UTPEE j terminó generando energía en el horizonte previo
array[1..J] of int: F; % Costo fijo de la operación de la UTPEE j
array[1..J] of float: V; % Costo variable de la operación de la UTPEE j
array[1..J] of int: P_inf; % Limite inferior de generación de potencia de la UTPEE j
array[1..J] of int: P_sup; % Limite superior de generación de potencia de la UTPEE j
array[1..J] of int: Sup; % Limite superior de ampliación de potencia de la UTPEE j
array[1..J] of int: Inf; % Limite inferior de reducción de potencia de la UTPEE j
array[1..J] of int: P0; % Potencia generada por la UTPEE j justo antes de iniciar el horizonte de planificación
array[1..K] of int: D; % Demanda global de energía para el período k
array[1..K] of int: R; % Reserva especificada de energía para el período k

% VARIABLES

array[1..J, 1..K] of var int: P; % Potencia generada por la UTPEE j en el período k
array[1..J, 1..K] of var 0..1: On; % Indica si la UTPEE j se encendió en el período k
array[1..J, 1..K] of var 0..1: Off; % Indica si la UTPEE j se apagó en el período k
array[1..J, 1..K] of var 0..1: Gen; % Indica si la UTPEE j generó energía en el período k
array[1..J, 1..K] of var float: CostoUTPEE; % Indica el costo de la UTPEE j en el período k

% FUNCIÓN OBJETIVO

var float: CostoTotal;

constraint CostoTotal = sum(j in 1..J, k in 1..K) (
  (CostoUTPEE[j,k])
);

% RESTRICCIONES

% No Negatividad

constraint forall(j in 1..J, k in 1..K) (
  (P[j, k] >= 0)
);

% Limite Superior

constraint forall(j in 1..J, k in 1..K) (
  (P[j, k] <= P_sup[j])
);

% Cuando una UTPEE está generando energía, la potencia generada no puede ser inferior
% a un mínimo permitido ni superior a un máximo permitido para esa planta.

constraint forall(j in 1..J, k in 1..K) (
  (P[j, k] >= P_inf[j] * Gen[j, k])
);

constraint forall(j in 1..J, k in 1..K) (
  (P[j, k] <= P_sup[j] * Gen[j, k])
);

% Si la UTPEE j generó energía en períodos consecutivos, entonces el cambio de
% generación de potencia entre el período k-1 y el período k no puede ser superior
% ni inferior a unos límites de ampliación y reducción establecidos

constraint forall(j in 1..J, k in 2..K)(
  if (P[j, k-1] > 0 /\ P[j, k] > 0)
    then
      (P[j, k] - P[j, k-1]) <= Sup[j]
  endif
);

constraint forall(j in 1..J, k in 2..K)(
  if (P[j, k-1] > 0 /\ P[j, k] > 0)
    then
      (P[j, k-1] - P[j, k]) <= Inf[j]
  endif
);

constraint forall(j in 1..J, k in 1..1) (
  if (G[j] = 1 /\ P0[j] > 0 /\ P[j, k] > 0)
    then
      (P[j, k] - P0[j]) <= Sup[j]
  endif
);

constraint forall(j in 1..J, k in 1..1) (
  if (G[j] = 1 /\ P0[j] > 0 /\ P[j, k] > 0)
    then
      (P0[j] - P[j,k]) <= Inf[j]
  endif
);

% Si la UTPEE j NO generó energía en un período k-1 y SÍ generó energía en el período
% período k, significa que la UTPEE j fue encendida en el período k

constraint forall(j in 1..J, k in 2..K) (
  if (P[j, k-1] = 0 /\ P[j, k] > 0)
    then
      (On[j,k] = 1)
    else
      (On[j,k] = 0)
  endif
);

constraint forall(j in 1..J, k in 1..1) (
  if (G[j] = 0 /\ P0[j] = 0 /\ P[j, k] > 0)
    then
      (On[j,k] = 1)
    else
      (On[j,k] = 0)
  endif
);

% Si la UTPEE j SÍ generó energía en un período k-1 y NO generó energía en el período
% período k, significa que la UTPEE j fue apagada en el período k

constraint forall(j in 1..J, k in 2..K) (
  if (P[j, k-1] > 0 /\ P[j, k] = 0)
    then
      (Off[j,k] = 1)
    else
      (Off[j,k] = 0)
  endif
);

constraint forall(j in 1..J, k in 1..1) (
  if (G[j] = 1 /\ P0[j] > 0 /\ P[j, k] = 0)
    then
      (Off[j,k] = 1)
    else
      (Off[j,k] = 0)
  endif
);

% Indica si la UTPEE j generó energía en el período k

constraint forall(j in 1..J, k in 1..K) (
  if (P[j, k] > 0)
  then
    (Gen[j,k] = 1)
  else
    (Gen[j, k] = 0)
  endif
);

% La suma de la potencia de las UTPEE en un período k debe 
% ser igual a la demanda global de energía para ese período

constraint forall(k in 1..K) (
  sum(j in 1..J) (P[j, k]) = D[k]
);

% Indica la potencia total disponible en el período k

constraint forall(k in 1..K) (
  sum(j in 1..J) (P_sup[j] * Gen[j,k]) >= (D[k] + R[k])
);

% Indica el costo unitario de la UTPEE j en el período k

constraint forall(j in 1..J, k in 1..K) (
  CostoUTPEE[j,k] = (F[j] * Gen[j, k] + V[j] * P[j, k] + E[j] * On[j, k] + A[j] * Off[j, k])
);

solve minimize CostoTotal;

output("Costo: \(CostoTotal), P: \(P)")
