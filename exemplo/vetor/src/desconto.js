/**
 * Regra de desconto da Vetor, plataforma ficticia de e-commerce B2B do workshop.
 *
 * Faixas sobre o valor total do pedido:
 *   ate 500,00          -> 0%
 *   500,01 a 2.000,00   -> 5%
 *   2.000,01 a 5.000,00 -> 10%
 *   acima de 5.000,00   -> 15%
 *
 * O desconto nunca ultrapassa TETO_DESCONTO por pedido.
 */

export const TETO_DESCONTO = 1000;

/**
 * @param {number} valorTotal valor do pedido em reais
 * @param {string} tipoCliente 'padrao' ou 'atacado'
 * @returns {number} valor do desconto em reais
 */
export function calcularDesconto(valorTotal, tipoCliente) {
  if (typeof valorTotal !== 'number' || Number.isNaN(valorTotal) || valorTotal < 0) {
    throw new TypeError('valorTotal deve ser um numero nao negativo');
  }

  let percentual = 0;
  if (valorTotal > 5000) {
    percentual = 0.15;
  } else if (valorTotal > 2000) {
    percentual = 0.1;
  } else if (valorTotal > 500) {
    percentual = 0.05;
  }

  return Math.min(valorTotal * percentual, TETO_DESCONTO);
}
