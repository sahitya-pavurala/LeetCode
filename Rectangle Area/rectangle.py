class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = abs(A-C) * abs(B-D)
        area2 = abs(E-G) * abs(F-H)
        
        if C < E or A > G:
            return area1 + area2
        elif B > H or D < F:
            return area1 + area2
        
        #elif A > E and C < G and B > F and D < H:
            
        
        else:
            
            inter_lbx = max(A,E)
            inter_lby = max(B,F)
            
            inter_rtx = min(C,G)
            inter_rty = min(D,H)
            
            overlap = abs(inter_lbx-inter_rtx) * abs(inter_lby-inter_rty)
            
            
            return area1 + area2 - overlap