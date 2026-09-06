import assert from 'node:assert/strict';
import { describe, it } from 'node:test';

import { calcularDesconto, TETO_DESCONTO } from '../src/desconto.js';

describe('calcularDesconto', () => {
  it('nao da desconto ate 500,00', () => {
    assert.equal(calcularDesconto(500, 'padrao'), 0);
  });

  it('da 5% na faixa de 500,01 a 2.000,00', () => {
    assert.equal(calcularDesconto(1000, 'padrao'), 50);
  });

  it('da 10% na faixa de 2.000,01 a 5.000,00', () => {
    assert.equal(calcularDesconto(3000, 'padrao'), 300);
  });

  it('da 15% acima de 5.000,00', () => {
    assert.equal(calcularDesconto(6000, 'padrao'), 900);
  });

  it('respeita o teto de desconto por pedido', () => {
    assert.equal(calcularDesconto(100000, 'padrao'), TETO_DESCONTO);
  });

  it('recusa valor negativo', () => {
    assert.throws(() => calcularDesconto(-1, 'padrao'), TypeError);
  });
});
