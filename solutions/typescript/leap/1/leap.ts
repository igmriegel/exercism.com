export function isLeap(year: number): boolean {
  const divByFour = year % 4 === 0;
  const divByHundred = year % 100 === 0;
  const divByFourHund = year % 400 === 0;

  if(divByFour && divByHundred) {
    return divByFourHund
  }

  return divByFour;
}
