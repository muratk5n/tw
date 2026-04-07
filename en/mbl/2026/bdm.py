from typing import List, Tuple, Dict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class A0x1:
    v1: str
    v2: float
    v3: float
    v4: float
    v5: float
    v6: float = 0.5
    v7: float = 0.5

class P0x2:
    def __init__(self, d1: List[A0x1], r1: float = 100.0):
        self.d1 = d1
        self.r1 = r1
        self.r2 = 100.0
        self.h1 = []
        
    def _u(self, p1: A0x1, p2: A0x1) -> float:
        c1 = 1.0 - (abs(p1.v2 - p2.v2) / self.r1)
        c2 = 1.0 - (abs(p1.v3 - p2.v3) / self.r2)
        return max(0.0, np.sqrt(max(0, c1) * max(0, c2)))
    
    def _p(self, p1: A0x1, p2: A0x1) -> float:
        w1 = p1.v4 * p1.v5 * self._u(p1, p2)
        w2 = p2.v4 * p2.v5 * self._u(p2, p1)
        return w1 / (w1 + w2) if (w1 + w2) != 0 else 0.5
    
    def _c(self, p1: A0x1, p2: A0x1, f1: float) -> bool:
        return abs(f1 - p2.v2) <= (p2.v3 / 100.0) * self.r1
    
    def _g(self, p1: A0x1, p2: A0x1, pr: float) -> float:
        rd = 0.8 if p2.v7 > 0.6 else 1.0
        ag = np.clip(pr * p1.v6 * rd + ((p1.v3 - p2.v3) / 200.0), 0.0, 1.0)
        return (p1.v2 * ag + p2.v2 * (1 - ag))
    
    def _b(self, i: int):
        if i < 2 or len(self.h1) < 2: return
        for s in self.d1:
            dp = abs(self.h1[-1]['p'].get(s.v1, s.v2) - self.h1[-2]['p'].get(s.v1, s.v2))
            s.v6 = min(0.9, s.v6 + 0.1) if dp < 2.0 else max(0.1, s.v6 - 0.05)
            s.v7 = min(0.9, s.v7 + 0.1) if dp < 2.0 else max(0.1, s.v7 - 0.05)
    
    def _step(self, i: int) -> Tuple[List[A0x1], Dict]:
        self._b(i)
        props = []
        for a in self.d1:
            for b in self.d1:
                if a == b: continue
                pv = self._p(a, b)
                prop = self._g(a, b, pv)
                cr = self._c(a, b, prop)
                props.append({'f': a.v1, 't': b.v1, 'p': prop, 'k': cr, 'w': a.v4 * a.v5 if cr else 0})
        
        nd = []
        for s in self.d1:
            cp = [p for p in props if p['t'] == s.v1 and p['k']]
            tw = sum(p['w'] for p in cp)
            if not cp or tw == 0:
                nd.append(s)
                continue
            wp = sum(p['p'] * p['w'] for p in cp) / tw
            dm = 0.3 + (s.v3 / 200.0)
            nv = (s.v2 * (1 - dm) + wp * dm)
            nd.append(A0x1(s.v1, nv, s.v3, s.v4, s.v5, s.v6, s.v7))
            
        st = {'i': i, 'p': {s.v1: s.v2 for s in nd}, 'b': {s.v1: (s.v6, s.v7) for s in nd}}
        return nd, st

    def run(self, m: int = 30, t: float = 0.5) -> Dict:
        for i in range(1, m + 1):
            self.d1, s = self._step(i)
            self.h1.append(s)
            if i > 5:
                rc = [abs(self.h1[j]['p'][n] - self.h1[j-1]['p'][n]) for j in range(-2, -1) for n in self.h1[j]['p']]
                if np.mean(rc) < t: break
        
        tw = sum(s.v4 * s.v5 for s in self.d1)
        res = sum(s.v2 * (s.v4 * s.v5) / tw for s in self.d1)
        return {'res': res, 'fin': {s.v1: s.v2 for s in self.d1}, 'h': self.h1}

def run_simulation(path: str):
    df = pd.read_csv(path)
    pts = [A0x1(r['Actor'], r['Position'], r['Resolve'], r['Clout'], r['Salience']) for _, r in df.iterrows()]
    eng = P0x2(pts)
    out = eng.run(t=0.3)
    
    print(f"\nValue: {out['res']:.2f}")
    for s in pts:
        fv = out['fin'][s.v1]
        print(f"{s.v1}: {s.v2:.2f} -> {fv:.2f} ({fv-s.v2:+.2f})")

