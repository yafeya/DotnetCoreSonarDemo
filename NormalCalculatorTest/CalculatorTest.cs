using NormalCalculationLib;
using System;
using Xunit;

namespace NormalCalculatorTest
{
    public class CalculatorTest
    {
        [Fact]
        public void Add_EQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.Equal(2, calculator.Add(1, 1));
        }

        [Fact]
        public void Add_NonEQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.NotEqual(0, calculator.Add(1, 1));
        }

        [Fact]
        public void Substract_EQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.Equal(0, calculator.Substract(1, 1));
        }

        [Fact]
        public void Substract_NonEQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.NotEqual(1, calculator.Substract(1, 1));
        }

        [Fact]
        public void Multiply_EQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.Equal(1, calculator.Multiply(1, 1));
        }

        [Fact]
        public void Multiply_NonEQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.NotEqual(1, calculator.Multiply(1, 3));
        }

        [Fact]
        public void Division_EQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.Equal(0.5, calculator.Division(1, 2));
            Assert.Equal(double.NaN, calculator.Division(1, 0));
        }

        [Fact]
        public void Division_NonEQ_Test()
        {
            var calculator = new NormalCalculator();
            Assert.NotEqual(0.5, calculator.Division(1, 3));
        }
    }
}
