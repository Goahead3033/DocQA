from inference import Inference
import time
#start_time = time.time()
infer = Inference()

#context = "余男（、），祖籍湖南湘潭，生于辽宁大连，中国电影女演员。1995年，在陪高中同学报考北京电影学院表演系时，被“意外”录取。余男自2000年主演电影《月蚀》后，就展现其精湛演技。尤其在《惊蛰》一片中的表现，为她囊括该年度中国境内几乎所有重要的奖项，更凭著《图雅的婚事》在柏林夺得金熊奖。由于其英语、法语皆流利，更将演艺版图拓展至欧美大陆，曾参与了法国电影《狂怒》（Fureur）、好莱坞动作片《权杖》（Diamond Dogs）、《极速赛车手》（Speed Racer）等片的演出。作为一位出色的中国女演员，余男一直以她的国际路线和特立独行而倍受瞩目。能熟练用英、法两门外语的余男，签约于美国最著名的经纪公司CAA，曾与众多优秀导演合作，而余男加盟《敢死队2》，也是中国女星真正打入好莱坞超黄金阵容，参与商业巨制的第一次尝试，是好莱坞动作片第一次启动中国女演员挑大梁出演女主角。"
#query = "作为一位出色的中国女演员，余男一直因为什么而倍受瞩目？"
#answer = infer.response(context,query)
#print(answer)
#end_time = time.time()
#print("the time of extracting answer from passage: ", end_time-start_time)


class DocQA:
	def __init__(self, query, context):
		self.query = query
		self.context = context
	def DocAnswer(self):
		answer = infer.response(self.context, self.query)
		return answer
if __name__ == '__main__':
	context = "余男（、），祖籍湖南湘潭，生于辽宁大连，中国电影女演员。1995年，在陪高中同学报考北京电影学院表演系时，被“意外”录取。余男自2000年主演电影《月蚀》后，就展现其精湛演技。尤其在《惊蛰》一片中的表现，为她囊括该年度中国境内几乎所有重要的奖项，更凭著《图雅的婚事》在柏林夺得金熊奖。由于其英语、法语皆流利，更将演艺版图拓展至欧美大陆，曾参与了法国电影《狂怒》（Fureur）、好莱坞动作片《权杖》（Diamond Dogs）、《极速赛车手》（Speed Racer）等片的演出。作为一位出色的中国女演员，余男一直以她的国际路线和特立独行而倍受瞩目。能熟练用英、法两门外语的余男，签约于美国最著名的经纪公司CAA，曾与众多优秀导演合作，而余男加盟《敢死队2》，也是中国女星真正打入好莱坞超黄金阵容，参与商业巨制的第一次尝试，是好莱坞动作片第一次启动中国女演员挑大梁出演女主角。"
	query = "作为一位出色的中国女演员，余男一直因为什么而倍受瞩目？"
	docqa = DocQA(query, context)
	answer = docqa.DocAnswer()
	print(answer)
	