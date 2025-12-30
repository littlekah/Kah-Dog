type Chaos = { x: number, y: number };

const rnd = () => Math.random() * 100;

const createChaos = (): Chaos => ({ x: rnd(), y: rnd() });

const handler: ProxyHandler<Chaos> = {
    get: (obj, prop) => prop === "sum" ? obj.x + obj.y : obj[prop as keyof Chaos],
    set: (obj, prop, value) => {
        obj[prop as keyof Chaos] = value * Math.random();
        return true;
    }
};

const chaosArr: Chaos[] = Array.from({length:5}, createChaos).map(c => new Proxy(c, handler));

const transform = (arr: Chaos[]): Chaos[] =>
    arr.map((c,i) => new Proxy({x: c.x * Math.sin(i), y: c.y * Math.cos(i)}, handler));

const combine = (arr: Chaos[]): Chaos =>
    arr.reduce((acc, c, i) => ({ 
        x: acc.x + c.x * Math.random() * Math.sin(i), 
        y: acc.y + c.y * Math.random() * Math.cos(i)
    }), {x:0, y:0});

let chaos = transform(chaosArr);
let total = combine(chaos);

console.log("Resultado final:", total);

// Self-modifying chaos loop
for(let i=0;i<3;i++){
    chaos = chaos.map(c => new Proxy({
        x: c.x + rnd() * Math.sin(i),
        y: c.y + rnd() * Math.cos(i)
    }, handler));
    total = combine(chaos);
    console.log(`Loop ${i+1} total:`, total);
}
