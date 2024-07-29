import { Button, Input, InputNumber, notification } from 'antd';
import axios from 'axios';
import { Controller, SubmitHandler, useForm } from 'react-hook-form';

import "./App.scss";
import { Form } from './App.styled';
import { useEffect } from 'react';

interface IUser {
  cpf: string;
  age: number;
}

const App = () => {
  const [api, contextHolder] = notification.useNotification();

  const { control, handleSubmit } = useForm({
    defaultValues: {
      cpf: "",
      age: 0
    },
  })

  const onSubmit: SubmitHandler<IUser> = async (data: { cpf: any; age: any; }) => {
    console.log(21, data);
    try {
      const response = await axios.post("http://localhost:8000/users/", data);
      if (response.status === 201) {
        api.success({
          message: `Notification - new user`,
          description: `User's CPF: ${data.cpf}. User's age: ${data.age}.`
        });
      }
    } catch(err) {
      api.error({
        message: `Notification - new user`,
        description: JSON.stringify((err as any).response.data)
      });
    }
  }

  useEffect(() => {
    (async () => {
      const response = await axios.get("http://localhost:8000/users");
      if (response.status === 200) {
        response.data.forEach((user: IUser) => {
          console.log(user);
        });
      }
    })();
  }, []);

  return (
    <div className="h-100 d-flex justify-content-center align-items-center">
      {contextHolder}
      <div className="card p-3">
        <div className="d-flex flex-column align-items-center">
          <img className="logo-duopen" src="https://i0.wp.com/useduopen.com.br/wp-content/uploads/2024/02/logo-colorida-1.png" />
          <Form onFinish={handleSubmit(onSubmit) as any}>{/* "as any" added here because of limitation from styled(Form) */}
            <Form.Item label="CPF">
              <Controller
                name="cpf"
                control={control}
                render={({ field }) => <Input {...field} />}
              />
            </Form.Item>

            <Form.Item label="Age">
              <Controller
                name="age"
                control={control}
                render={({ field }) => <InputNumber {...field} />}
              />
            </Form.Item>

            <Form.Item>
              <div className="d-flex justify-content-center">
                <Button htmlType="submit">new user</Button>
              </div>
            </Form.Item>
          </Form>
        </div>
      </div>
    </div>
  )
}

export default App;
