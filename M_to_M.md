# Many to many relationships

: 한 테이블이 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우, 양쪽 모두에서 N:1의 관계를 가짐

### N : 1의 한계 

복수의 외래키를 참조하기 위해서는 객체를 하나 더 만들어야 함

허나 외래 키 컬럼에 'a, b' 형태로 저장하는 건 DB 타입 문제로 불가능 

### 중개 모델

양 쪽 모델에서 서로 N:1 관계를 가지는 중개 모델 생성

예시) 
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)      # doctor 모델과 N:1 관계 
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)    # patient 모델과 N:1 관계 

        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'


Django에서는 'ManytoManyField'로 중개 모델을 자동으로 생성 가능

## ManyToManyField

: M : N 관계 설정 모델 필드 

두 모델 중 어떤 모델에 작성해도 상관 없음, 참조/역참조 관계를 잘 기억할 것 

add, remove 같은 쿼리 사용 가능 (다 대 다 관계)

'through' : 중개 테이블에 '추가 데이터'를 사용해 M:N 관계를 형성하려는 경우에 사용 -> 대신 자동으로 생성해주는 모델이 아닌 직접 작성해야 함 -> ManyToManyField의 argument로 직접 만든 중개 모델 지정 


예시)

        class Doctor(models.Model):
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 의사 {self.name}'


        class Patient(models.Model):
            doctors = models.ManyToManyField(Doctor, through='Reservation')
            name = models.TextField()

            def __str__(self):
                return f'{self.pk}번 환자 {self.name}'


        class Reservation(models.Model):
            doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
            patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
            symptom = models.TextField()
            reserved_at = models.DateTimeField(auto_now_add=True)

            def __str__(self):
                return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'

1. 참조하는 모델 : patient2.doctors.remove(doctor1)

2. 역참조 모델 : doctor1.patient_set.remove(patient1)



