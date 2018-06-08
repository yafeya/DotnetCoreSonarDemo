using SuperCalculationLib;
using System;
using Xunit;

namespace SuperCalculatorTest
{
    public class CalculatorTest
    {
        [Fact]
        public void Pow_EQ_Test()
        {
            var calculator = new SuperCalculator();
            Assert.Equal(4, calculator.Pow(2, 2));
            Assert.Equal(2, calculator.Pow(4, 0.5));
            Assert.Equal(0.25, calculator.Pow(4, -1));
        }

        [Fact]
        public void Pow_NonEQ_Test()
        {
            var calculator = new SuperCalculator();
            Assert.NotEqual(0.25, calculator.Pow(5, -1));
        }
    }
}
