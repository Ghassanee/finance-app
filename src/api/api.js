import axios from "axios";
const API = "http://127.0.0.1:5000";
export async function getInfo(actif, option) {
  try {
    const response = await axios.get(
      `${API}/info?actif=${actif}&option=${option}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function getIndice(indice) {
  try {
    const response = await axios.get(`${API}/indice?indice=${indice}`);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function getIndicatorDeLiquidity(
  actif_name,
  option,
  pt,
  date_deb,
  date_fin
) {
  try {
    const response = await axios.get(
      `${API}/indicator_de_liquidity?actif_name=${actif_name}&option=${option}&pt=${pt}&date_deb=${date_deb}&date_fin=${date_fin}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function PlotIndicateurDrawdown(actif_name, tp) {
  try {
    const response = await axios.get(
      `${API}/plot_indicateur_drawdown?actif_name=${actif_name}&tp=${tp}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function PlotActifLine(actif_name) {
  try {
    const response = await axios.post(`${API}/plot_actif_line`, {
      actif_name,
    });
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function RisqueActif(actif_name, date_debut, date_fin) {
  try {
    const response = await axios.post(`${API}/risque_actif`, {
      actif_name,
      date_debut,
      date_fin,
    });
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function PlotIndicateurMA(actif_name, longueur) {
  try {
    const response = await axios.post(`${API}/plot_indicateur_ma`, {
      actif_name,
      longueur,
    });
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function CombinaisonIndicateurs(
  actif_name,
  cible_indicateur,
  longueur_MA
) {
  try {
    const response = await axios.post(`${API}/combinaison_indicateurs`, {
      actif_name,
      cible_indicateur,
      longueur_MA,
    });
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function PlotHistogramme(actif_name) {
  try {
    const response = await axios.get(
      `${API}/plot_histogramme?actif_name=${actif_name}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

export async function CovarianceMatrice(actif_name, date_debut, date_fin) {
  try {
    const response = await axios.post(`${API}/covariance_matrice`, {
      actif_name,
      date_debut,
      date_fin,
    });
    return response.data;
  } catch (error) {
    console.log(error);
  }
}
