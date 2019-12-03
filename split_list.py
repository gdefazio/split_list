__author__ = 'Giuseppe Defazio'

class list(list):

    def split_list(self, chunks):
        'Return a list containing the splitted input list in chunks'
        length = len(self)
        chunks = int(chunks)
        chunklen = length / chunks
        div = list(range(0, length, int(chunklen)))
        div.append(None)
        chunks_indexes = list(zip(div[:-1], div[1:]))
        chunk_list = list()
        for t in chunks_indexes:
            chunk_list.append(self[t[0]:t[1]])

        return chunk_list
