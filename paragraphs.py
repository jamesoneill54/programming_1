import sys

def format_paragraphs(s):
   s = s.split(' ')
   paragraphs = []
   current = []
   i = 0
   while i < len(s):
      if '\n\n' not in s[i]:
         current.append(s[i])
      else:
         par_end, par_start = s[i].split('\n\n')[0], s[i].split('\n\n')[-1]
         current.append(par_end)
         paragraphs.append(current)
         current = [par_start]
      i += 1
   paragraphs.append(current)
   return paragraphs


def format_sentences(lines):
   endings = '.!?'
   sentences = []
   current = []

   i = 0
   while i < len(lines):
      line = lines[i].strip().split()
      j = 0
      while j < len(line):
         current.append(line[j])
         if line[j][-1] in endings:
            current[0] = current[0].capitalize()
            sentences.append(' '.join(current))
            current = []
         j += 1
      i += 1

   return '\n'.join(sentences)


def main():
   lines = sys.stdin.read().strip()
   separated_pars = format_paragraphs(lines)
   paras = []
   i = 0
   while i < len(separated_pars):
      paras.append(format_sentences(separated_pars[i]))
      i += 1
   print '\n\n'.join(paras)

if __name__ == '__main__':
   main()