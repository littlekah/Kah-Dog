using System;
using System.Collections.Generic;

class ChaosObject
{
    public float X;
    public float Y;

    public ChaosObject(float x, float y)
    {
        X = x;
        Y = y;
    }

    public static ChaosObject operator +(ChaosObject a, ChaosObject b)
    {
        return new ChaosObject(a.X + b.X, a.Y + b.Y);
    }

    public override string ToString()
    {
        return $"({Math.Round(X,2)},{Math.Round(Y,2)})";
    }
}

class Program
{
    static Random rnd = new Random();

    static ChaosObject RandomObject()
    {
        return new ChaosObject((float)rnd.NextDouble()*100, (float)rnd.NextDouble()*100);
    }

    static ChaosObject Transform(List<ChaosObject> list)
    {
        List<ChaosObject> result = new List<ChaosObject>();
        for(int i = 0; i < list.Count; i++)
        {
            result.Add(new ChaosObject(
                (float)(list[i].X * Math.Sin(i)),
                (float)(list[i].Y * Math.Cos(i))
            ));
        }
        ChaosObject sum = new ChaosObject(0,0);
        foreach(var c in result)
        {
            sum += c;
        }
        return sum;
    }

    static void Main()
    {
        List<ChaosObject> objs = new List<ChaosObject>();
        for(int i=0;i<5;i++)
            objs.Add(RandomObject());

        ChaosObject total = Transform(objs);
        Console.WriteLine("Resultado final: " + total);
    }
}
