import axios from "axios";
const API = "http://127.0.0.1:5000";
export function getInfo(actif, option) {
  return axios
    .get(`${API}/info?actif=${actif}&option=${option}`)
    .then(function (response) {
      return response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
}

export function getIndice(indice) {
  return axios
    .get(`${API}/indice?indice=${indice}`)
    .then(function (response) {
      return response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
}

export function getIndicatorDeLiquidity(
  actif_name,
  option,
  pt,
  date_deb,
  date_fin
) {
  return axios
    .get(
      `${API}/indicator_de_liquidity?actif_name=${actif_name}&option=${option}&pt=${pt}&date_deb=${date_deb}&date_fin=${date_fin}`
    )
    .then(function (response) {
      return response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
}
