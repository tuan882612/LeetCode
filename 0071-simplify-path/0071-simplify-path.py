class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        res = []
        
        for dir in path.split('/'):
            if dir not in '../':
                res.append(dir)
            elif dir == '..' and res:
                res.pop()
                
        return '/' + '/'.join(res)