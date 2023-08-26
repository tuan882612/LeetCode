class Solution:
    def simplifyPath(self, path: str) -> str:
        ref = '../ '
        if len(path) == 1 and path not in ref:
            return '/'

        dirs = path.split('/')
        res = []
        
        for dir in dirs:
            if dir not in ref:
                res.append(dir)
            elif dir == '..' and res:
                res.pop()
                
        return '/'+'/'.join(res)