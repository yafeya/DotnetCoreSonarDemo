using System;

namespace NormalCalculationLib
{
    public class NormalCalculator
    {
        public int Add(int a, int b)
        {
            return a + b;
        }

        public int Substract(int a, int b)
        {
            return a - b;
        }

        public int Multiply(int a, int b)
        {
            return a * b;
        }

        public double Division(int a, int b)
        {
            double result = double.NaN;
            if (b != 0)
            {
                result = (double)a / (double)b;
            }
            return result;
        }
    }
}
