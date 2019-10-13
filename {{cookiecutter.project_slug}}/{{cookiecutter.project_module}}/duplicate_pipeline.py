# -*- coding: utf-8 -*-


from scrapy.exceptions import DropItem


class DuplicatePipeline(object):

    def __init__(self):
        self.items_senn = set()
        
    def process_item(self,item,spider):
        hash_item = hash(frozenset(item.items()))
        if hash_item  in self.items_senn:
            raise DropItem("Duplicate item found: {}".format(item))
        else:
            self.items_senn.add(hash_item)
            return item
