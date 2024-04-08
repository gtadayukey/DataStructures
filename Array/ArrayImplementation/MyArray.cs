namespace ArrayImplementation
{
    class MyArray<T>()
    {
        private int _length = 0;
        private T[] _data = new T[1];

        public T Get(int index)
        {
            return _data[index];
        }

        public void Push(T value)
        {

            if (_length == _data.Length)
            {
                T[] tempData = new T[_length];
                Array.Copy(_data, tempData, _length);
                _data = new T[_length + 1];
                Array.Copy(tempData, _data, _length);
            }

            _data[_length] = value;
            _length++;
        }

        public void Pop()
        {
            _data[^1] = default;
            _length--;
        }

        public void Delete(int index)
        {
            ShiftItems(index);
            _data[^1] = default;
            _length--;
        }

        private void ShiftItems(int index)
        {
            for(int i = index; i < _length - 1; i++)
            {
                _data[i] = _data[i + 1];
            }
        }


        public override string ToString()
        {
            if (_length == 0)
            {
                return "Nothing to see here...";
            }

            string arrayString = "[";

            for (var i = 1; _length > i; i++)
            {
                arrayString += _data[i - 1].ToString() + ", ";
            }

            arrayString += _data[_length - 1] + "]";

            return arrayString;
        }
    }
}
