import pytorch
import torch.nn as nn
import torch.optim as optim

# класс для нашей модели RNN с LSTM-слоями:
class RNNModel(nn.Module):
    def __init__(self, input_size, output_size, hidden_dim, n_layers):
        super(RNNModel, self).__init__()

        self.hidden_dim = hidden_dim

        self.rnn = nn.LSTM(input_size, hidden_dim, n_layers, batch_first=True)

        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x, hidden):
        batch_size = x.size(0)

        r_out, hidden = self.rnn(x, hidden)

        r_out = r_out.view(-1, self.hidden_dim)

        output = self.fc(r_out)

        return output, hidden

# оптимизатор
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# цикл обучения
n_epochs = 1000

for epoch in range(1, n_epochs + 1):
    optimizer.zero_grad()

    hidden = model.init_hidden(batch_size)

    for i, batch in enumerate(train_loader):
        inputs, labels = batch
        hidden = tuple([each.data for each in hidden])

        outputs, hidden = model(inputs, hidden)

        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        if i%100 == 0:
            print('Epoch: {}/{}...'.format(epoch, n_epochs),
                  'Loss: {:.4f}'.format(loss.item()))
