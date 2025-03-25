from django.db import models
# 게시글(Article) 모델 정의
class Article(models.Model):
    title = models.CharField(max_length=100)
    A = models.TextField(null=True, blank=True)
    B = models.TextField(null=True, blank=True)
    # comment_set: Comment 모델과의 역참조 관계 (Django에서 자동 생성)
CATEGORY = (
    ('A', 'A'),
    ('B', 'B')
)
# 댓글(Comment) 모델 정의
class Comment(models.Model):
    answer = models.CharField(max_length=20, choices=CATEGORY, default='A')
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 게시글과의 외래키 관계 (게시글 삭제 시 댓글도 삭제)
    # article_id: Article 모델의 id를 참조 (Django에서 자동 생성)



