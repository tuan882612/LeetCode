class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        
        for dir in path.split('/'):
            if dir not in '../':
                res.append(dir)
            elif dir == '..' and res:
                res.pop()
                
        return '/' + '/'.join(res)